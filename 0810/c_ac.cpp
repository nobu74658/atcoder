#include <iostream>
#include <vector>
#include <string>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int Q;
    std::cin >> Q;
    const int N = 1000000;
    std::vector<int> box(N, 0);
    int non_zero_count = 0;

    for (int i = 0; i < Q; ++i) {
        std::string query;
        std::cin >> query;
        if (query == "1") {
            int x;
            std::cin >> x;
            if (box[x - 1] == 0) {
                non_zero_count++;
            }
            box[x - 1] += 1;
        } else if (query == "2") {
            int x;
            std::cin >> x;
            if (box[x - 1] == 1) {
                non_zero_count--;
            }
            box[x - 1] -= 1;
        } else {
            std::cout << non_zero_count << std::endl;
        }
    }

    return 0;
}
