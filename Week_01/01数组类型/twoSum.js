function twoSum(nums, target) {
    let i = 0;
    let j = nums.length - 1
    let res = []
    while (i < j) {
        // 条件
        if ( nums[i] +  nums[j] == target) {
            console.log(1, i, j)
            res = [i, j]
            break
        }else if ( nums[i] +  nums[j] < target) {
            console.log(2, i, j)
            i++
        }else {
            console.log(3, i, j)
            j--
        }
    }
    return res
};

twoSum([2,7,11,15], 9)
// console.log(1)