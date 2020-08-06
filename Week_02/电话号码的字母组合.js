// 终于有所理解了；后面多看几篇
// 原来这个也叫做DFS
// 其实就是理解成树，时间复杂度为2^n

var letterCombinations = function(digits) {
    if(!digits){
        return []
    }
    
    let res = []
    let len = digits.length

    var map = new Map();
    map.set('2','abc');
    map.set('3','def');
    map.set('4','ghi');
    map.set('5','jkl');
    map.set('6','mno');
    map.set('7','pqrs');
    map.set('8','tuv');
    map.set('9','wxyz');

    function _generate(i, str){
        // terminator
        if( i >= len ) {
            res.push(str)
            return
        }
        // process
        // drill down
        var _str = map.get(digits[i])
        console.log(_str, i, len)
        for(var j = 0; j < _str.length; j++) {
            _generate(i+1, _str[j] + str)
        }
    }

    _generate(0, '')
    return res
};

console.log(letterCombinations("23"))
