class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if not input_list:
            return input_list

        max_value = input_list[0]
        for num in input_list:
            if num > max_value:
                max_value = num

        return [max_value if x > 0 else x for x in input_list]

    @staticmethod
    def search(input_list: list[int], query: int) -> int:

        left, right = 0, len(input_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if input_list[mid] == query:
                return mid
            elif input_list[mid] < query:
                left = mid + 1
            else:
                right = mid - 1
        return -1

