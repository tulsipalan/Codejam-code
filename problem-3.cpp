
Problem-3
Cameron and Jamie's kid is almost 3 years old! However, even though the child is more independent now, scheduling kid activities and domestic necessities is still a challenge for the couple.

Cameron and Jamie have a list of N activities to take care of during the day. Each activity happens during a specified interval during the day. They need to assign each activity to one of them, so that neither of them is responsible for two activities that overlap. An activity that ends at time t is not considered to overlap with another activity that starts at time t.

For example, suppose that Jamie and Cameron need to cover 3 activities: one running from 18:00 to 20:00, another from 19:00 to 21:00 and another from 22:00 to 23:00. One possibility would be for Jamie to cover the activity running from 19:00 to 21:00, with Cameron covering the other two. Another valid schedule would be for Cameron to cover the activity from 18:00 to 20:00 and Jamie to cover the other two. Notice that the first two activities overlap in the time between 19:00 and 20:00, so it is impossible to assign both of those activities to the same partner.

Given the starting and ending times of each activity, find any schedule that does not require the same person to cover overlapping activities, or say that it is impossible.

Solution:
The Solution is in C++


#include<bits/stdc++.h>
#define ll long long

int main(int argc, char const *argv[])
{

    int m, k;
    std::cin >> m;
    for (int k = 0; k < m; k++)
    {
        std::string s;
        int i, n;
        std::cin >> n;
        std::vector<std::pair<int, std::pair<int, int>>> v;
        int st[n], en[n];
        for (int i = 0; i < n; i++)
        {

            std::cin >> st[i] >> en[i];
            v.push_back({st[i], {en[i], i}});
            s += 'C';
        }

        std::sort(v.begin(), v.end());
        int c1 = 0, j = 0, flag1 = 0;
        for (int i = 0; i < v.size(); i++)
        {

            if (v[i].first >= c1)
            {
                s[v[i].second.second] = 'C';
                c1 = v[i].second.first;
            }

            else if (v[i].first >= j)
            {
                s[v[i].second.second] = 'J';
                j = v[i].second.first;
            }

            else
            {
                flag1 = 1;
                break;
            }
        }
        if (flag1 == 1)
        {
            std::cout << "Case #" << k + 1 << ": "
                      << "IMPOSSIBLE" << std::endl;
            continue;
        }
        std::cout << "Case #" << k + 1 << ": " << s << std::endl;
    }
    return 0;
}