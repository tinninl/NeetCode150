import java.util.HashMap;

public class TwoSum {
    
    public int[] twoSum(int[] nums, int target){

        int[] result = {-1,-1};

        HashMap<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++){

            int diff = target - nums[i];

            if (seen.containsKey(diff)){

                result[0] = i;
                result[1] = seen.get(diff);
                
                break;

            }

        }

        return result;

    }

}
