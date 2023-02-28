/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let result = [];
    let temp = 0;
    for (let i = 0; i < nums.length; i++){
        temp += nums[i];
        result.push(temp);
    }
    return result;
};
// [1,2,3]
/// temp = 1
// result = [1]

// temp = (1) + 2 = 3
// result = [1,3]

// temp = (1+2) + 3 == 6
// result = [1,3,6]