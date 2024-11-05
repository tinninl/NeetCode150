public class TrappingRainWater {
    
    public int trap(int[] height){

        int n = height.length;

        if (n == 0)
            return 0;

        int area = 0, totalArea = 0;

        int maxLeft = 0, maxRight = 0;

        int[] left = new int[n];
        int[] right = new int[n];

        for (int i = 0; i < n; i++){
            left[i] = maxLeft;

            if (height[i] > maxLeft)
                maxLeft = height[i];

        }

        for (int i = n - 1; i >= 0; i--){
            right[i] = maxRight;
            if(height[i] > maxRight)   
                maxRight = height[i];
        }

        for (int i = 0; i < n; i++){
            area = Math.min(left[i], right[i]) - height[i];
            if (area > 0)
                totalArea += area;
        }

        return totalArea;
    }

    public int trap2(int[] height){

        if (height.length == 0)
            return 0;

        int area = 0, totalArea = 0;

        int l = 0, r = height.length - 1;

        int maxLeft = 0, maxRight = 0;

        while (l <= r){

            if (maxLeft < maxRight){
                area = Math.max(maxLeft - height[l], 0);

                if (height[l] > maxLeft)
                    maxLeft = height[l];
                l++;
            }

            else {
                area = Math.max(maxRight - height[r], 0);

                if (height[r] > maxRight)
                    maxRight = height[r];
                r--;
            }

            totalArea += area;
        }

        return totalArea;
    }

}
