public class ValidPalindrome {

    public boolean isValidPalindrome(String s){

        int l = 0, r = s.length() - 1;  // left and right pointers

        while (l < r){

            // Skip whitespaces
            while(!Character.isLetterOrDigit(s.charAt(r)))
                r--;

            while(!Character.isLetterOrDigit(s.charAt(l)))
                l++;

            // Check pairs of letters
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r)))
                return false;   

            // Update pointers
            l++;
            r--;
            
        }

        return true;

    }

}
