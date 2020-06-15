class Solution {
    public int[] sortArray(int[] nums) {
        
        int size = nums.length;
        
        for(int i = 1; i < size; i++){
            
            int key = nums[i];
            int j = i-1;
            
            while(j >= 0 && nums[j] > key){
                
                nums[j+1] = nums[j];
                j--;
            }
            
            nums[j+1] = key;            
        }
        return nums;
    }
}
