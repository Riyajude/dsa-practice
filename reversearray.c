#include <stdio.h>
void reverse(int arr[],int size){
    int revarr[size];
    for(int i=0;i<size;i++){
        revarr[i]=arr[size-i-1];
    }
    printf("Reversed array: ");
    for(int i=0;i<size;i++){
        printf("%d ",revarr[i]);
    }
}
int main() {
    int size;
    printf("Enter size\n");
    scanf("%d",&size);
    int arr[size];
    printf("Enter elements\n");
    for(int i=0;i<size;i++){
        scanf("%d",&arr[i]);
    }
    reverse(arr,size);
    return 0;
}
