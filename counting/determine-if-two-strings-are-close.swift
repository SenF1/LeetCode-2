class Solution {
    func closeStrings(_ word1: String, _ word2: String) -> Bool {
        
        if word1.count != word2.count {return false}
        
        let w1 = Array(word1), w2 = Array(word2)
        var dic1 = [Character:Int](), dic2 = [Character:Int]()
        
        for i in 0..<word1.count{
            dic1[w1[i], default:0] += 1
            dic2[w2[i], default:0] += 1
        }
        
        if dic1.keys != dic2.keys 
        || dic1.values.sorted() != dic2.values.sorted(){
            return false
        }
        
        return true
    }
}