def analyze_monkey_str(str):

    def population1_rule1(words, index):
        original_index = index
        result, index = population1_rule2(words, index)
        if result:
            return True, index

        index = original_index
        if index < len(words) and words[index] == "ау":
            index += 1
            result, index = population1_rule2(words, index)
            if result:
                return True, index
        
        return False, original_index

    def population1_rule2(words, index):
        original_index = index
        result, index = population1_rule3(words, index)
        if result:
            return True, index

        index = original_index
        if index < len(words) and words[index] == "ку":
            index += 1
            result, index = population1_rule3(words, index)
            if result:
                return True, index
        
        return False, original_index

    def population1_rule3(words, index):
        if index < len(words) and words[index] == "ух-ты":
            return True, index + 1
        
        original_index = index
        if index < len(words) and words[index] == "хо":
            index += 1
            result, index = population1_rule3(words, index)
            if result:
                return True, index
        
        index = original_index
        if index < len(words) and words[index] == "ну":
            index += 1
            result, index = population1_rule1(words, index)
            if result and index < len(words) and words[index] == "и_ну":
                return True, index + 1
        
        return False, original_index

    def population2_rule1(words, index):
        if index < len(words) and words[index] == "ой":
            index += 1
            result, index = population2_rule2(words, index)
            if result and index < len(words) and words[index] == "ай":
                index += 1
                result, index = population2_rule3(words, index)
                if result:
                    return True, index
        
        return False, index

    def population2_rule2(words, index):
        original_index = index
        if index < len(words) and words[index] == "ну":
            return True, index + 1

        index = original_index
        if index < len(words) and words[index] == "ну":
            index += 1
            result, index = population2_rule2(words, index)
            if result:
                return True, index
        
        return False, original_index

    def population2_rule3(words, index):
        if index < len(words) and words[index] == "ух-ты":
            return True, index + 1
        
        original_index = index
        if index < len(words) and words[index] == "хо":
            index += 1
            result, index = population2_rule3(words, index)
            if result and index < len(words) and words[index] == "хо":
                return True, index + 1
        
        return False, original_index

    words = str.split()
    
    result1, index1 = population1_rule1(words, 0)
    if result1 and index1 == len(words):
        return "Это говорит обезьяна из первой популяции"

    result2, index2 = population2_rule1(words, 0)
    if result2 and index2 == len(words):
        return "Это говорит обезьяна из второй популяции"

    return "Это говорит неместная обезьяна"

# Например:
# Ну ух-ты и_ну  - это говорит обезьяна из первой популяции.
# Ой ну ай ух-ты - это говорит обезьяна из второй популяции.
# Ну ой ау - это говорит неместная обезьяна.

print(analyze_monkey_str("ну ух-ты и_ну"))
print(analyze_monkey_str("ой ну ай ух-ты"))
print(analyze_monkey_str("ну ой ау"))

print(analyze_monkey_str("ух-ты ау ну и_ну ку ух-ты ку ну  и_ну ку ух-ты ау ух-ты ау хо ну ой  ну  и_ну"))
print(analyze_monkey_str("ух-ты ну  и_ну"))

print(analyze_monkey_str("хо хо хо ну  и_ну ку хо хо хо ух-ты"))
print(analyze_monkey_str("ух-ты ау   хо хо хо   ну  и_ну ку хо ну  и_ну ау ух-ты ау ух-ты ау   ух-ты ау   ну  и_ну ау ну ой ух-ты какой и_ну"))
print(analyze_monkey_str("хо ух-ты ау ну  и_ну ку хо хо   хо хо ух-ты ку ух-ты ку хо ух-ты ау хо ой"))
print(analyze_monkey_str("ух-ты ку ух-ты"))
print(analyze_monkey_str("ух-ты ку хо ух-ты хо"))
