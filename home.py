class Home:
    def __init__(self,number):
        self.number = number

    def get_number(self):
        return self.number

    def is_even(self):
        return self.number % 2 == 0
    
    def is_odd(self):
        return self.number % 2 != 0

    def is_price(self):
        ans = []
        for i in range(1,self.number+1):
            if self.number // i == self.number / i:
                ans.append(i)
        return len(ans) == 2   

    def get_divisors(self):
        ans = []
        for i in range(1,self.number+1):
            if self.number // i == self.number / i:
                ans.append(i)
        return ans
    
    def get_length(self):
        return len(str(self.number))

    def get_sum(self):
        ans = 0
        number = str(self.number)
        for i in number:
            ans += int(i)
        return ans

    def get_product(self):
        ans = []
        for i in str(self.number):
            ans.append(i)
        return ans
    def get_reverse(self):
        a = list(str(self.number))
        a.reverse()
        return int(''.join(a))
    def get_digits(self):
        ans = list(str(self.number))
        return ans
    def get_max(self):
        ans = list(str(self.number))
        max = 0
        for i in ans:
            if int(i) > max:
                max = int(i)
        return max
    def get_min(self):
        ans = list(str(self.number))
        min = 9
        for i in ans:
            if int(i) < min:
                min = int(i)
        return min
    def get_average(self):
        ans = list(str(self.number))
        average = 0
        for i in ans:
            average += int(i)
        return average/len(ans)
    def get_median(self):
        ans = list(str(self.number))
        a = []
        for i in ans:
            a.append(int(i))
        a.sort()
        if len(ans) % 2 == 0:
            return a[len(ans)//2-1:len(ans)//2+1]
        else:
            return a[len(ans)//2]
    def get_mode(self):
        a = []
        ans = list(str(self.number))
        for i in ans:
            a.append(ans.count(i))
        s = zip(ans,a)
        g = 0
        d = ''
        for i, j in s:
            if j > g:
                g = j
                d = i
        return d

    def get_range(self):
        a = []
        for i in range(self.number):
            a.append(i)
        return a
    def get_frequency(self):
        ans = list(str(self.number))
        a = []
        for i in range(1,len(str(self.number))+1):
            a.append(i)
        s = zip(a,ans)
        d = {}
        for i, j in s:
            d[i] = int(j)
        return d
x = Home(number = 11)
print(x.get_frequency())