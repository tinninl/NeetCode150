public class ContainerWithMostWater {
    
    public int maxArea(int[] heights){

        int l = 0, r = heights.length - 1;  // left and right pointers

        int area = 0, maxArea = 0;

        int h, w;   // height and width, respectively

        while (l < r){

            // Calculate height, width, and area
            h = Math.min(heights[l], heights[r]);
            w = r = l;
            area = h * w;

            // Check maxArea
            if (area > maxArea)
                maxArea = area;

            // Shift pointer
            if (heights[l] > heights[r])
                r--;

            else
                l++;

        }

        return maxArea;

    }

}
