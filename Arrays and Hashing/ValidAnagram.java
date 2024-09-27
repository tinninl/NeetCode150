public class ValidAnagram {

    public boolean isAnagram(String s, String t){

        if (s.length() != t.length())
            return false;

        int[] store1 = new int[26];
        int[] store2 = new int[26];

        for (int i = 0; i < s.length(); i++){

            store1[s.charAt(i) - 'a']++;
            store2[t.charAt(i) - 'a']++;

        }

        for (int i = 0; i < store1.length; i ++)

            if (store1[i] != store2[i])

                return false;

        return true;

    }

}
