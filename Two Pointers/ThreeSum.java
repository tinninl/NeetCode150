import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {

    public List<List<Integer>> threeSum(int[] nums, int target){

        List<List<Integer>> res = new ArrayList<>();

        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++){

            if (nums[i] > 0)
                break;

            if ((nums[i] == nums[i - 1]) && (i > 0))
                continue;

            int l = i + 1, r = nums.length - 1;

            while (l < r){

                int threeSum = nums[i] + nums[l] + nums[r];

                if (threeSum < 0)
                    l++;
                else if (threeSum > 0)
                    r--;

                else{
                    ArrayList<Integer> miniRes = new ArrayList<>();
                    miniRes.add(nums[i]);
                    miniRes.add(nums[l]);
                    miniRes.add(nums[r]);
                    res.add(miniRes);
                    
                    l++;
                    r--;
                    while (nums[l] == nums[l - 1] && l < r)
                    l++;
                }
            }

            
        }

        return res;
    }
}