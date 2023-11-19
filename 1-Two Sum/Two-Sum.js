/**** 
 * https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU
 * https://leetcode.com/problems/two-sum/
 ****/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    //create a hashmap to store complement values
    map = {};
    for(let i=0; i<nums.length; i++) {
        let value = nums[i];
        let complementPair = target - value;
        if(map[complementPair] !== undefined) {
            return [ map[complementPair], i ];
        } else {
            map[value] = i;
        }

    }
    
};

console.log( twoSum([0, 1, 2, 3, 4, 55, 44], 99) )