#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <cjson/cJSON.h> 
#include <stdint.h>

#define SERVICENAME "KCSC SERVICE"
#define  VERSION "1.0.0"
#define STATUS "RUNNING"

enum CODE{
    HEARTBEAT_CHECK,
    INFO,
    WRITE_LOG,
};

struct header {
    int code ;
    uint32_t sound_info_size ;
    uint32_t video_info_size;
};

void hearbeat_report()
{
    char heart_beat_report_buffer[0x100];
    memset(heart_beat_report_buffer, 0, sizeof(heart_beat_report_buffer));
    time_t rawtime;
    struct tm *timeinfo;
    char time_string[100];  
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    strftime(time_string, sizeof(time_string), "%Y-%m-%d %H:%M:%S", timeinfo);
    snprintf(heart_beat_report_buffer, sizeof(heart_beat_report_buffer),
             "Current Time: %s\nSERVICE NAME: %s\nVERSION: %s\nSTATUS: %s",
             time_string, SERVICENAME, VERSION, STATUS);
    puts(heart_beat_report_buffer);
}

void info(uint32_t sound_info_size, uint32_t video_info_size) {
    uint64_t video_info_array[100] = {0};
    uint64_t sound_info_array[100] = {0};

    if (sound_info_size + video_info_size > ((sizeof(sound_info_array) + (sizeof(video_info_array)) / sizeof(uint64_t)))) {
        puts("Packet too big to handle!!!!!");
        return;
    }
    char *buffer = calloc(0x1000, 1); 

    if (!buffer) {
        puts("Memory allocation failed!!!!!");
        return;
    }

    size_t read_size = read(0, buffer, 0x1000);
    if (read_size <= 0) {
        puts("Failed to read input!!!!!");
        free(buffer);
        return;
    }
    cJSON *json = cJSON_Parse(buffer);
    if (!json) {
        puts("Malformed packet!!!!!");
        free(buffer);
        exit(0);
    }
    cJSON *sound = cJSON_GetObjectItem(json, "sound_info");
    if (sound && cJSON_IsArray(sound)) {
        int index = 0;
        cJSON *current_element = NULL;
        cJSON_ArrayForEach(current_element, sound) {
            if (cJSON_IsNumber(current_element)) {
                sound_info_array[index] = (uint64_t)current_element->valuedouble;
            } else {
                puts("Invalid data type in sound_info array.");
            }
            index++;
            if(index == sound_info_size)
            {
                break;
            }
        }
    }
    cJSON *video = cJSON_GetObjectItem(json, "video_info");
    if (video && cJSON_IsArray(video)) {
        int index = 0;
        cJSON *current_element = NULL;
        cJSON_ArrayForEach(current_element, video) {
            if (cJSON_IsNumber(current_element)) {
                video_info_array[index] = (uint64_t)current_element->valuedouble;
            } else {
                puts("Invalid data type in video_info array.");
            }
            index++;
            if(index == video_info_size)
            {
                break;
            }
        }
    }
    cJSON_Delete(json); 
    free(buffer);        
}

#define log_file_magic 0xDEADBEEF

struct log_file_info{
    int magic;
    uint32_t content_len;
    char *content_buf;
};

int checksum(uint16_t * buffer,int len)
{
    uint32_t sum = 0;
    for(uint32_t i = 0 ; i < len ; i++)
    {
        sum += buffer[i];
    }
    return sum;
}
void write_log()
{   
    char heart_beat_report_buffer[0x100];
    memset(heart_beat_report_buffer, 0, sizeof(heart_beat_report_buffer));
    time_t rawtime;
    struct tm *timeinfo;
    char time_string[100];  
    char buffer_log_content[0x200];
    struct log_file_info log_header = {0};
    read(0,&log_header,12);
    if(log_header.magic != log_file_magic)
    {
        puts("Unknow Message");
        return ;
    }

    if(log_header.content_len > sizeof(buffer_log_content))
    {
        log_header.content_buf = calloc(log_header.content_len,1);
        if(log_header.content_buf==NULL)
        {
            puts("Malloc Failed");
            return;
        }
    }else{
        log_header.content_buf = &buffer_log_content;
    }
    read(0,log_header.content_buf,log_header.content_len);
    uint32_t sum = checksum(log_header.content_buf,log_header.content_len);
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    strftime(time_string, sizeof(time_string), "%Y-%m-%d %H:%M:%S", timeinfo);
    snprintf(heart_beat_report_buffer, sizeof(heart_beat_report_buffer),
             "LOG Time: %s\nSERVICE NAME: %s\nVERSION: %s\nSTATUS: %s\nCHECKSUM ON LOG CONTENT : %u",
             time_string, SERVICENAME, VERSION, STATUS,sum);
    puts(heart_beat_report_buffer);
}

void init(){
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);
}

int main()
{
    init();
    struct header *h = calloc(sizeof(h),1) ;
    while(1)
    {
        memset(h,0,sizeof(h));
        read(0,h,sizeof(struct header));
        switch (h->code){
            case HEARTBEAT_CHECK:
                hearbeat_report();
                break;
            case INFO:
                info(h->sound_info_size,h->video_info_size);
                break;
            case WRITE_LOG:
                write_log();
                break;
        } 
    }
    return 0;
}