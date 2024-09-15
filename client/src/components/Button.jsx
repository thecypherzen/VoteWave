import { Link } from 'react-router-dom';
import '../styles/button.css';


export default function Button({
	href=null, id=null, clist=[],
	clickHandler=null, text
}){
	let element;
	let items = null;

	if (clist.length){
		let len = clist.length;
		items = "";
		for (let i = 0; i < len; i++){
			items += clist[i];
			if (i < len - 1){
				items += " ";
			}
		}
	}
	if (href){
		element = <Link to={href} id={id}
		className={items ? items : ""}
		onClick={ clickHandler }>
			{text}
		</Link>;
	} else {
		element = <button type="button" id={id}
		className={items ? items : ""}
		onClick={ clickHandler } >
			{text} </button>
	}

	return (<>{element}</>);
}