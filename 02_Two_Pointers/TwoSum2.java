public class TwoSum2 {
    
    public int[] twoSum2(int[] nums, int target){

        int[] res = {-1,-1};

        int l = 0, r = nums.length - 1;

        int sum;

        while (l < r){

            sum = nums[l] + nums[r];

            if (sum < target)
                l++;
            
            else if (sum > target)  
                r--;

            else {
                res[0] = l + 1;
                res[1] = r + 1;
                break;
            }

        }

        return res;

    }

}
