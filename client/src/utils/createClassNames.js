export function classNameFromList(list=null){
	let className = "";

	if (list) {
		const len = list.length;
		for (let i = 0; i < len; i++){
			className += `${list[i]}`;
			if (i < len - 1){
				className  += ' ';
			}
		}
	}
	return className;
}