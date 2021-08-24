#include <stdlib.h>
#include <string.h>

#include "list.h"

//List init
void list_init(List *list, void (*destroy)(void *data)){

	list->size = 0;
	list->destroy = destroy;
	list->head = NULL;
	list->tail = NULL;
	return;
}

//List destroy
void list_destroy(List *list){
	void *data;
	//remove each element

	while(list_size(list)>0){
		if(list_rem_next(list, NULL, (void **)&data) == 0 && list->destroy!=NULL) {
			//call a user defined destroy function to free the data
			list->destroy(data);
		}
	}

	//No operations are allowed on the structure but clear the structure as a precaution
	memset(list, 0, sizeof(list));

	return;
}





