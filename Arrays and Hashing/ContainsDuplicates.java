import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicates{

    public boolean hasDuplicate(int[] nums){

        Set<Integer> uniques = new HashSet<>();
        
        for (int i = 0; i < nums.length; i++) {

            if (uniques.contains(nums[i])) 
                return true;
        
            else
                uniques.add(nums[i]);

        }

        return false;

    }

}