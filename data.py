# file to organise variables used in the server

class STATUS:
    UNDER_REVIEW = 'Under Review'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'


# Key code should contain URL-safe and filename-safe chars only
TEAMS = {
    "team-a": "Team A",
    "team-b": "Team B",
    "team-c": "Team C",
    "team-d": "Team D",
    "team-e": "Team E",
    "team-f": "Team F",
    "team-g": "Team G",
}


SESSIONS = {
    # '<ip>':'team'
}

SOLVES = {
    s: {
        #'<chalcode>': {'time':datetime, 'status':STATUSES}
    } for s in TEAMS
}

# challenge page details
CHALLENGES = [
    ('c01', 'Target Practice', '''You are in the American army, training to be a sniper to vanquish the German state. You are given n target balloons, indexed from 0 to n - 1. Each target is painted with a number on it represented by an array nums. You are asked to shoot all the targets.

If you shoot the ith target, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by shooting the targets.

Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:
Input: nums = [1,5]
Output: 10
 
Constraints:
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100

Python:
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
Java:
class Solution {
    public int maxCoins(int[] nums) {
        
    }
}

C++:
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        
    }
};
.'''),

    ('c02', 'Coding Coordinates', '''You are attempting to find the coordinates of a spy in the army. You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.
You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order to locate the spy.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists

Python:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

Java:
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
    }
}

C++:
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
    }
};
 '''),

    ('c03', 'Minecraft: Operation Freefall', '''In the heart of the conflict, the Allies have devised a daring new training exercise to test the reflexes and navigating skills of their most elite operatives. 
    
This exercise, called the Dropper Course, is a high-altitude descent into enemy territory. 

The objective is to navigate through a vertical maze and reach the ground without taking damage. 

The Dropper Course is designed to train soldiers to experience the conditions of a warzone, with narrow gaps, sudden drops, and obstacles that demand quick reflexes and sharp focus. Upon successfully completing the series of descents, you will obtain a crucial secret code. This code is vital for decrypting enemy communications and could turn the tide of the conflict in favour of the Allies.

1. Open Minecraft and enter the world named Challenge #3
2. Complete the obstacle course and obtain a code.
3. Decode the code and submit the final message obtained. Online converters can be used for decoding.'''),

    ('c04', 'Find the Spy!', '''You have recently realised that there is a spy in your army camp. In your efforts, you have narrowed the imposter down to 5 people. Each of these people are of a different nationality, have a different drink of choice, a different brand of cigar, a different favourite dictator and a different favourite item. They all live in 5 consecutive houses.  You know that the imposter’s item will be the documents which give you the codes to the nuclear weaponry.  Your surveillance has picked up a list of information about the 5 suspects:

The Englishman smokes Lucky Strike
The Japanese man keeps his letters from home
The German drinks tea.
The Camel smoker is to the left of the Chesterfield smoker.
The Camel smoker drinks coffee.
The supporter of Hitler owns a rifle
The Dunhill smoker supports Alexander the Great
The person that lives in the middle house drinks milk. 
The American lives in the first house. 
The supporter of Napoleon lives next to the grenade owner
The person who treasures their coins lives next to the follower of Alexander the Great
The follower of Stalin drinks wine. 
The Soviet supports Mussolini
The American lives next to an Old Gold smoker
The devotee of Napoleon lives next to the whiskey drinker

What is the nationality of the imposter?'''),

    ('c05', 'Decryption Algorithms', '''Debug the following flawed code in one of the following languages:

Problem: To decrypt a secret message you have received, you must write a function to convert binary to decimal

Python:
def decimal(num):
    decimal_val = 0
    base = 2
    while num > 0:
        rem = num // 10
        decimal_val = rem ** base
        num = num % 10
        base = base ** 2
    return decimal_val

#main
print(decimal(101010101111010))       #Expected output: 21882 

Java:
public class c05 {
    public static void main(String[] args) {
        System.out.println(decimal(101010101111010L)); // Note the 'L' to denote a long literal
    }

    public static long decimal(long num) {
        long decimalVal = 0;
        long base = 2;
        
        while (num > 0) {
            long rem = num / 10;
            decimalVal = rem ** base;
            num = num % 10;
            base = base ** 2;
        }
        
        return decimalVal;
    }
}

C++:
#include <iostream>
using namespace std;

int decimal(long long num) {
    int decimal_val = 0;
    int base = 2;
    while (num > 0) {
        int rem = num / 10;
        decimal_val += pow(rem, base);
        num = num % 10;
        base = base * base;
    }
    return decimal_val;
}

int main() {
    long long num = 101010101111010;
    cout << decimal(num) << endl; // Expected output: 21882
    return 0;
}'''),

    ('c06', 'Escape the Maze', '''Debug the following flawed code in one of the following languages:
    
Problem: The following function is supposed to count all possible paths from the top-left corner to the bottom-right corner of a board (m x n), given that you can only move down and right. On reaching the bottom corner, you will finally be able to escape the maze.

Python:
def count_paths(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return count_paths(m+1, n) + count_paths(m, n+1)

#Test the function
print(count_paths(3, 3))   #Expected output: 6
print(count_paths(4, 3))   #Expected output: 10

Java:
public class Main {
    public static void main(String[] args) {
        System.out.println(countPaths(3, 3)); // Expected output: 6
        System.out.println(countPaths(4, 3)); // Expected output: 10
    }

    public static int countPaths(int m, int n) {
        if (m == 1 || n == 1) {
            return 1;
        } else {
            return countPaths(m + 1, n) + countPaths(m, n + 1);
        }
    }
}

C++:
#include <iostream>
using namespace std;

int count_paths(int m, int n) {
    if (m == 1 || n == 1) {
        return 1;
    } else {
        return count_paths(m + 1, n) + count_paths(m, n + 1);
    }
}

int main() {
    int m = 3, n = 3; // Example values
    cout << "Number of paths: " << count_paths(m, n) << endl;  // Expected output: 6

    int p = 4, q = 3; // Example values
    cout << "Number of paths: " << count_paths(p, q) << endl;  // Expected output: 10

    return 0;
}'''),


    ('c07', 'Jump Those Hoops!', '''You must complete an obstacle course, where you have to jump through hoops to escape. You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.
Return true if you can reach the last hoop (index) starting from index 0, or false otherwise.

Example 1:
Input: nums = [1,2,0,1,0]
Output: True
Explanation: First jump from index 0 to 1, then from index 1 to 3, and lastly from index 3 to 4.

Example 2:
Input: nums = [1,2,1,0,1]
Output: False

Constraints:
1 <= nums(length) <= 1000
0 <= nums[i] <= 1000

Python:
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

Java:
class Solution {
    public boolean canJump(int[] nums) {
        
    }
}

C++:
class Solution {
public:
    bool canJump(vector<int>& nums) {
        
    }
};
'''),

    ('c08', 'Time Troubles', '''You are given a string s representing a 12-hour format time, the exact time when your ships will be attacked,  where some of the digits (possibly none) are replaced with a "?".

12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59. The earliest 12-hour time is 00:00, and the latest is 11:59.

You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is a valid 12-hour format time and is the latest possible, to save your ships.

Return the resulting string.

Example 1:
Input: s = "1?:?4"
Output: "11:54"
Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "11:54".

Example 2:
Input: s = "0?:5?"
Output: "09:59"
Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "09:59".

Constraints:
s.length == 5
s[2] is equal to the character ":".
All characters except s[2] are digits or "?" characters.
The input is generated such that there is at least one time between "00:00" and "11:59" that you can obtain after replacing the "?" characters.

Python:
class Solution(object):
    def findLatestTime(self, s):
        """
        :type s: str
        :rtype: str
        """

Java:
class Solution {
    public String findLatestTime(String s) {
        
    }
}

C++:
class Solution {
public:
    string findLatestTime(string s) {
        
    }
};
'''),
    
    ('c09', 'Minecraft: Operation Skyfall', '''In the midst of the war, the Allies have uncovered a revolutionary flight machine known as the Elytra. 

The Elytra could offer advantages in aerial reconnaissance and swift tactical strikes. 

Before it can be used in combat, the Elytra needs thorough testing to prove its capabilities. You have been selected for this critical mission. 

As a top pilot, your objective is to navigate through an obstacle course designed to mimic the treacherous conditions of a battlefield. 

This course is packed with narrow passes and sharp turns that will push your flying skills to the limit. Successfully complete the course to validate the Elytra’s effectiveness and earn a secret code essential to the Allied effort. This code holds the key to unlocking new strategies and securing a decisive victory.

1. Open Minecraft and enter the world named Challenge #9
2. Complete the course and obtain a code.
3. Decode the code and submit the final message obtained. Online converters can be used for decoding.'''),


    ('c10', 'Decrypt the Code!', '''In the heart of World War II, a crucial encrypted message has been intercepted from Axis forces. This message is encoded using a five-digit self-descriptive number, revealing strategic plans. Your mission is to crack the code and uncover the vital information hidden within.
The encrypted message is a five-digit self-descriptive number.
A self-descriptive number is an integer m that is b digits long in which each digit d at position n (the most significant digit being at position 0 and the least significant at position b−1) counts how many instances of digit n are in m.
For example, in number 1210,
The first digit (1) indicates that there is one 0 in the number.
The second digit (2) indicates that there are two 1s in the number.
The third digit (1) indicates that there is one 2 in the number.
The fourth digit (0) indicates that there are zero 3s in the number.

There is exactly one 5 digit self-descriptive number, and you cannot decode the intercepted message without it. What is the number?'''),
    
    ('c11', 'River Escape', '''In the course of your escape, you come across a river. You have with you a wolf, a goat and a cabbage.  You have a boat, but it can only carry you and one other item at a time. If left alone together, the wolf will eat the goat, and the goat will eat the cabbage. What is the minimum number of trips (where a trip refers to crossing the river one way) required to transport you and all 3 items safely?'''),
    
    ('c12', 'First Failure', '''Debug the following flawed code in one of the following languages:
    
For a number that is palindromic and a perfect cube its cube root is also a palindrome. For example 11^3 = 1331. What is the first cube that fails this property? 

Python:
def is_palindrome(n):
    return s == s[::-1]

def find_first_failure():
    n = 1
    while True:
        cube = n ** 3
        cube_root = int(round(cube  (1/3)))
        if cube_root ** 3 == cube and is_palindrome(cube) and not is_palindrome(cube_root):
            return n
        n += 1

first_failure = find_first_failure()
print("The first number that fails the property is:”, first_failure)
#Expected Output: 10662526601


Java:
public class Main {
    public static void main(String[] args) {
        long firstFailure = findFirstFailure();
        System.out.println("The first number that fails the property is: " + firstFailure); // Expected Output: 10662526601
    }

    public static boolean isPalindrome(long n) {
        return s.equals(new StringBuilder(s).reverse().toString());
    }

    public static long findFirstFailure() {
        long n = 1;
        while (true) {
            long cube = n * n * n;
            long cubeRoot = Math.round(Math.cbrt(cube));
            if (cubeRoot * cubeRoot * cubeRoot == cube && isPalindrome(cube) && !isPalindrome(cubeRoot)) {
                return n;
            }
            n++;
        }
    }
}


C++:
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

bool is_palindrome(long long n) {
    string rev_s = string(s.rbegin(), s.rend());
    return s == rev_s;
}

long long find_first_failure() {
    long long n = 1;
    while (true) {
        long long cube = n * n * n;
        long long cube_root = static_cast<long long>(round(pow(cube, 1.0 / 3)));
        if (cube_root * cube_root * cube_root == cube && is_palindrome(cube) && !is_palindrome(cube_root)) {
            return n;
        }
        n++;
    }
}

int main() {
    long long first_failure = find_first_failure();
    cout << "The first number that fails the property is: " << first_failure << endl;
    // Expected Output: 10662526601
    return 0;
} '''),
    
    ('c13', 'No Duplicates', '''You are cracking a code and will be unsuccessful if there are any duplicate characters in the encoded string, but you need to maximise the number of characters you are processing. Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Python:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

Java:
class Solution {
    public int lengthOfLongestSubstring(String s) {
        
    }
}

C++:
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
    }
};
'''),
    
    ('c14', 'Triangle of Strength', '''In the war, consider each row of Pascal's Triangle representing a different year of the war, with each number symbolising the strategic strength and alliances of the nations involved. Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

Python:
class Solution(object):
    def generate(self, numRows):
        """java
        :type numRows: int
        :rtype: List[List[int]]
        """

Java:
class Solution {
    public List<List<Integer>> generate(int numRows) {
        
    }
}

C++:
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        
    }
};
'''),
    
    ('c15', 'Minecraft: Operation Leap', '''In a daring effort to outmanoeuvre enemy forces, the Allies have constructed a parkour obstacle course to train their elite soldiers. 
    
This course is designed to simulate the agility and precision needed to navigate the treacherous landscapes during critical missions. The parkour course is laden with obstacles, requiring impeccable timing, swift movements, and acute awareness. Each segment of the course will contain checkpoints.

Upon completing the course, you will obtain a secret code essential for deciphering enemy plans and securing a strategic advantage in the war.

1. Open Minecraft and enter the world named Challenge #15
2. Complete the course and obtain a code.
3. Decode the code and submit the final message obtained. Online converters can be used for decoding.'''),

    
    ('c16', 'Minecraft: Operation Swift Step', '''In the heart of the conflict, the Allies have constructed a parkour obstacle course to train their elite soldiers. 
    
This course is designed to simulate the agility and precision needed to navigate the treacherous landscapes during critical missions. The parkour course is laden with obstacles, requiring impeccable timing, swift movements, and acute awareness. Each segment of the course will contain checkpoints.

Upon completing the course, you will obtain a secret code essential for deciphering enemy plans and securing a strategic advantage in the war.

1. Open Minecraft and enter the world named Challenge #16
2. Complete the course and obtain a code.
3. Decode the code and submit the final message obtained. Online converters can be used for decoding.'''),
    
    ('c17', 'Bridge Escape', '''You and your unit in the RAF have recently bombed an army base in Al Qaeda and are making your daring escape. Your unit consists of 5 members: you, the sniper, the hacker, the bombing specialist and the muscle. To make your escape, the 5 of you must cross the electric fence, and run to your waiting helicopter. You have only 1 light among the 5 of you, and it can illuminate a maximum of two people while crossing. No one can attempt to cross the fence without a light. There are no loopholes or tricks you can employ. The times taken by each of you are as follows (these times are all one way):
You: 1 minute to cross
Sniper: 2 minutes to cross
Bombing specialist: 5 minutes to cross
Muscle: 10 minutes to cross
Hacker: 15 minutes to cross

What is the minimum time taken for all 5 of you to escape?
'''),
    
    ('c18', 'A Fraction of Resources', '''Debug the following flawed code in one of the following languages:
    
Problem: Function to add 2 fractions

Python:
def gcd(a, b):
    while b:
        a, b = b, a // b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def add_fractions(fraction1, fraction2):
    num1, den1 = map(int, fraction1.split('/'))
    num2, den2 = map(int, fraction2.split('/'))
    lcd = lcm(den1, den2)
    new_num1 = num1 * (lcd // den1)
    new_num2 = num2 * (lcd // den2)
    new_num = new_num1 * new_num2
    common_divisor = lcm(new_num, lcd)
    simplified_num = new_num // common_divisor
    simplified_den = lcd * common_divisor
    return f"{simplified_num}/{simplified_den}"

#main
fraction1 = int(input("Enter the first fraction (e.g., '1/2'): "))       #  1/6
fraction2 = int(input("Enter the second fraction (e.g., '1/3'): "))    #  2/7
result = add_fractions(fraction1, fraction2)

print(f"The sum of {fraction1} and {fraction2} is {result}")      # Expected output: 19/42

Java:
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the first fraction (e.g., '1/2'): ");
        String fraction1 = scanner.nextLine();
        
        System.out.print("Enter the second fraction (e.g., '1/3'): ");
        String fraction2 = scanner.nextLine();
        
        String result = addFractions(fraction1, fraction2);
        
        System.out.println("The sum of " + fraction1 + " and " + fraction2 + " is " + result);
        
        scanner.close();
    }

    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a / b;
            a = temp;
        }
        return a;
    }

    public static int lcm(int a, int b) {
        return a * (b / gcd(a, b));
    }

    public static String addFractions(String fraction1, String fraction2) {
        String[] parts1 = fraction1.split("/");
        String[] parts2 = fraction2.split("/");
        
        int num1 = Integer.parseInt(parts1[0]);
        int den1 = Integer.parseInt(parts1[1]);
        
        int num2 = Integer.parseInt(parts2[0]);
        int den2 = Integer.parseInt(parts2[1]);
        
        int lcd = lcm(den1, den2);
        
        int newNum1 = num1 * (lcd / den1);
        int newNum2 = num2 * (lcd / den2);
        
        int newNum = newNum1 * newNum2; 
        int commonDivisor = lcm(newNum, lcd); 
        
        int simplifiedNum = newNum / commonDivisor;
        int simplifiedDen = lcd * commonDivisor; 
        
        return simplifiedNum + "/" + simplifiedDen;
    }
}


C++:
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a / b;
        a = temp;
    }
    return a;
}

int lcm(int a, int b) {
    return a * (b / gcd(a, b));
}

string add_fractions(const string& fraction1, const string& fraction2) {
    int num1, den1, num2, den2;
    sscanf(fraction1.c_str(), "%d/%d", &num1, &den1);
    sscanf(fraction2.c_str(), "%d/%d", &num2, &den2);
    int lcd = lcm(den1, den2);
    int new_num1 = num1 * (lcd / den1);
    int new_num2 = num2 * (lcd / den2);
    int new_num = new_num1 * new_num2;
    int common_divisor = lcm(new_num, lcd);
    int simplified_num = new_num / common_divisor;
    int simplified_den = lcd * common_divisor;
    stringstream result;
    result << simplified_num << "/" << simplified_den;
    return result.str();
}

int main() {
    string fraction1, fraction2;

    cout << "Enter the first fraction (e.g., '1/2'): ";  // 1/6
    cin >> fraction1;

    cout << "Enter the second fraction (e.g., '2/3'): ";   // 2/7
    cin >> fraction2;

    string result = add_fractions(fraction1, fraction2);
    cout << "The result of adding the fractions is: " << result << endl;   // Expected output: 19/42

    return 0;
}'''),
    
    ('c19', 'Bomb Squad', '''You are given an integer array nums representing the positions of your enemy's bombs.

In one move, you can choose one element of nums and change it to any value.

You can perform at most three moves without your enemy realising that you know where the bombs are and figuring out that you have classified information.

Minimise the damage and return the minimum difference between the largest and smallest value of nums after performing at most three moves.

 

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 2 to 3. nums becomes [5,3,3,4].
In the second move, change 4 to 3. nums becomes [5,3,3,3].
In the third move, change 5 to 3. nums becomes [3,3,3,3].
After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: We can make at most 3 moves.
In the first move, change 5 to 0. nums becomes [1,0,0,10,14].
In the second move, change 10 to 0. nums becomes [1,0,0,0,14].
In the third move, change 14 to 1. nums becomes [1,0,0,0,1].
After performing 3 moves, the difference between the minimum and maximum is 1 - 0 = 1.
It can be shown that there is no way to make the difference 0 in 3 moves.
Example 3:

Input: nums = [3,100,20]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 100 to 7. nums becomes [3,7,20].
In the second move, change 20 to 7. nums becomes [3,7,7].
In the third move, change 3 to 7. nums becomes [7,7,7].
After performing 3 moves, the difference between the minimum and maximum is 7 - 7 = 0.
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

Python:
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

Java:
class Solution {
    public int minDifference(int[] nums) {
        
    }
}

C++:
class Solution {
public:
    int minDifference(vector<int>& nums) {
        
    }
};
'''),
    
    ('c20', 'Imposter?', '''Given an integer array nums where every element is an agent code and an integer k which is the range in which all agents must have distinct codes, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k, which indicates that there is an imposter in your midst.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

Python:
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

Java:
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        
    }
}

C++:
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        
    }
};
'''),
    
    ('c21', 'The Frontline', '''You are given a non-negative integer array nums where each element represents the health level of an enemy soldier. In one operation, you must choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.
 
Example 1:
Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

Example 2:
Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.
 
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100

Python:
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

Java:
class Solution {
    public int minimumOperations(int[] nums) {
        
    }
}

C++:
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        
    }
};
'''),
    
    ('c22', 'Minecraft: Swift Stride', '''In the midst of the war, the Allies have constructed a parkour obstacle course to train their elite soldiers. 
    
This course is designed to simulate the agility and precision needed to navigate the treacherous landscapes during critical missions. The parkour course is laden with obstacles, requiring impeccable timing, swift movements, and acute awareness. Each segment of the course will contain checkpoints.

Upon completing the course, you will obtain a secret code essential for deciphering enemy plans and securing a strategic advantage in the war.

1. Open Minecraft and enter the world named Challenge #22
2. Complete the course and obtain a code.
3. Decode the code and submit the final message obtained. Online converters can be used for decoding.'''),
    
    ('c23', 'Unlock the Dials', '''You find yourself in front of a gate that requires a specific combination to unlock. The gate has 4 dials, each labelled with a different unit of data storage (Tera, Yotta, Zetta, and Peta). Each dial can be set to a number between 1 and 9. Your team gives you the following information they could find:
The dial with the largest unit of storage is set to an odd number that is not part of the fibonacci series.
The number on the dial equal to 1024 Exabytes is a prime number.
The dial representing the smallest unit of storage is an even number that is half of the highest even number in the dial
The combination does not include repeated numbers.
The sum of all four numbers is 20.
'''),
    
    ('c24', 'In a Fraction of Time', '''Debug the following flawed code in one of the following languages:
    
Problem: Consider the fraction n / d where n, d belong to the set of natural numbers. If n < d, HCF(n, d) = 1, it is called a reduced proper fraction. Find the number of reduced proper fractions for d < 2024.

def gcd(a, b):
    while b != 0:
        a, b = b, a // b
    return a

def count_reduced_proper_fractions(limit):
    count = 0
    for d in range(1, limit):
        for n in range(d, limit):
            if gcd(n, d) == 1:
                count += 1
    return count

limit = 2024
result = count_reduced_proper_fractions(limit)
print(f"The number of reduced proper fractions for d < {limit} is: {result}")    #Expected output: 1244843

Java:
public class Main {
    public static void main(String[] args) {
        int limit = 2024;
        int result = countReducedProperFractions(limit);
        System.out.println("The number of reduced proper fractions for d < " + limit + " is: " + result);   // Expected output: 1244843
    }

    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a / b;
            a = temp;
        }
        return a;
    }

    public static int countReducedProperFractions(int limit) {
        int count = 0;
        for (int d = 1; d < limit; d++) {
            for (int n = d; n < limit; n++) {
                if (gcd(n, d) == 1) {
                    count++;
                }
            }
        }
        return count;
    }
}


C++:
#include <iostream>

using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int count_reduced_proper_fractions(int limit) {
    int count = 0;
    for (int d = 2; d < limit; ++d) {
        for (int n = 1; n < d; ++n) {
            if (gcd(n, d) == 1) {
                ++count;
            }
        }
    }
    return count;
}

int main() {
    // Set the limit to 2024
    int limit = 2024;
    int result = count_reduced_proper_fractions(limit);
    cout << "The number of reduced proper fractions for d < " << limit << " is: " << result << endl;

    return 0;
}'''),
    
    ('c25', 'Climb to Freedom', '''You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:

Input: n = 2

Output: 2
Explanation:

1 + 1 = 2
2 = 2
Example 2:

Input: n = 3

Output: 3
Explanation:

1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3
Constraints:

1 <= n <= 30

Python:
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

Java:
class Solution {
    public int climbStairs(int n) {
        
    }
}

C++:
class Solution {
public:
    int climbStairs(int n) {
        
    }
};
'''),
]