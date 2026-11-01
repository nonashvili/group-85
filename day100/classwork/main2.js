let nums = [2, 3, 5, 6, 7, 9, 77, 47, 5, 4, 3, 27, 2]

for(let i = 0; i < nums.length; i++) {
    if(nums[i] > 50) {
        console.log("num which is greater than 50 is found " + nums[i])
        break
    }
    console.log(nums[i])
}