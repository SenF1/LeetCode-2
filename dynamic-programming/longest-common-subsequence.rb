# @param {String} text1
# @param {String} text2
# @return {Integer}
def longest_common_subsequence(text1, text2)
  
  indices = {}
  text1.each_char.with_index { |char1, index1| ( indices[char1] ||= [] ) << index1 }
  indices.transform_values!(&:reverse)
  
  result = []
  text2.each_char do |char2|
    
    indices[char2]&.each do |index1|
      index = result.bsearch_index { |val| val >= index1 }
      
      if index.nil? 
        result << index1 
      elsif result[index] > index1
        result[index] = index1 
      end
    
    end

  end

  result.size
end