
// See https://aka.ms/new-console-template for more information
//Console.WriteLine("Hello, World!");

public static int[] TwoSum(int[] nums, int target) {
    Dictionary<int, int> map = new Dictionary<int, int>();
    for(int i=0; i nums.length; i++) {
        value = nums[i];
        complement = target - value;
        if(trygetValue(map[value], out complementIndex))
            return [complementIndex, i];
        else
            
    }
}