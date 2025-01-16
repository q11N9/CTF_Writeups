/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De4_Word_Dict;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

/**
 *
 * @author maima
 */
public class Dictionary {
    private ArrayList<Word> words;

    public Dictionary() {
        words = new ArrayList<>();
        // Thêm 10 từ mẫu
        words.add(new Word("1", "apple", "quả táo"));
        words.add(new Word("2", "banana", "quả chuối"));
        words.add(new Word("3", "cat", "con mèo"));
        words.add(new Word("4", "dog", "con chó"));
        sortWords(); // Sắp xếp khi khởi tạo
    }

    // Tìm kiếm nhị phân
    public String binarySearch(String en) {
        int left = 0, right = words.size() - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            Word midWord = words.get(mid);

            int cmp = en.compareToIgnoreCase(midWord.getEn());
            if (cmp == 0) {
                return midWord.getVn();
            } else if (cmp < 0) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return null; // Không tìm thấy
    }
    // Thêm 1 từ vào trong từ điển
    public boolean addWord(String en, String vn) {
        for (Word word : words) {
            if (word.getEn().equalsIgnoreCase(en)) {
                return false; // Từ đã tồn tại
            }
        }
        // Set id tăng dần
        words.add(new Word(String.valueOf(words.size() + 1), en, vn));
        sortWords(); // Sắp xếp lại danh sách
        return true;
    }
    // Update 1 từ trong từ điển
    public boolean updateWord(String en, String newVn) {
        for (Word word : words) {
            if (word.getEn().equalsIgnoreCase(en)) {
                word.setVn(newVn);
                return true; // Cập nhật thành công
            }
        }
        return false; // Không tìm thấy từ để sửa
    }

    // Sắp xếp danh sách từ
    private void sortWords() {
        Collections.sort(words, Comparator.comparing(Word::getEn));
    }
}
