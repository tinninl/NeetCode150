import java.util.HashSet;

public class LongestSubstringWithoutRepeatingCharacters {

    public int longestSubstring(String s){

        int maxLength = 0;

        HashSet<Character> charSet = new HashSet<>();

        int left = 0, right = 0;

        for (; right < s.length(); right++){

            char c = s.charAt(right);

            while (charSet.contains(c)){
                charSet.remove(s.charAt(left));
                left++;
            }
        }
    }
}
