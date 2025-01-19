#include<stdio.h>

void dubblesort(int* arr, int size){
	if (size != -1){
		int x = size - 2;
		for(int* i = &arr[size - 1];; --i){
			if (x != -1){
				int* ptr = arr;
				do{
					int ptr_val = *ptr;
					int pivot = arr[1];
					if (*ptr > pivot){
						*ptr = pivot;
						arr[1] = ptr_val;
					}
					++ptr;
				}while (i != ptr);
				if (!x) break;
			}
			--x;
		}
	}
}
int main(){

}