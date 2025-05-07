/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) return head;
        // Step 1: Find the length of the list
        ListNode* curr = head;
        int length = 1;
        while (curr->next) {
            curr = curr->next;
            length++;
        }
        // Step 2: Make it a circular list
        curr->next = head;
        // Step 3: Find the new tail (length - k % length - 1) and new head (length - k % length)
        k = k % length;
        int steps = length - k;
        curr = head;
        for (int i = 1; i < steps; i++) {
            curr = curr->next;
        }
        // Step 4: Break the loop
        head = curr->next;
        curr->next = nullptr;

        return head;
    }
};
