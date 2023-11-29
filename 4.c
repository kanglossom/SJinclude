#include<stdio.h>
int ans= 2147483647;
void min(int i){
	if(i<ans) 
		ans = i;
}
main(){
	int sc[10]={18,77,68,54,99,15,56,97,64,48};
	int i;
	for(i=0;i<10;i++)
		min(sc[i]);
	printf("%d\n",ans);
}
