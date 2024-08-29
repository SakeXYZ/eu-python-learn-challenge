from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result_list = []
        for item in input_array:
            condition, result = func(item)
            if condition:
                result_list.append(result)
        return result_list
