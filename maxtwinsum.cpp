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
    int pairSum(ListNode* head) {
        //find mid
        ListNode* slow=head;
        ListNode* fast=head;
        while (fast && fast->next){
            slow=slow->next;
            fast=fast->next->next;
        }
        //rev ll
        ListNode* prev=nullptr;
        ListNode* curr=slow;
        while (curr) {
            ListNode* nextNode=curr->next;
            curr->next=prev;
            prev=curr;
            curr=nextNode;
        }
        //find twinsum
        ListNode* firstHalf = head;
        ListNode* secondHalf = prev;
        int maxSum = 0;
        while (secondHalf) {
            int twinSum = firstHalf->val + secondHalf->val;
            maxSum = max(maxSum, twinSum);
            firstHalf = firstHalf->next;
            secondHalf = secondHalf->next;
        }

        return maxSum;
    }
};
