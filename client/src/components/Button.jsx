import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import '../styles/button.css';


export default function Button({
	href=null, id=null, clist=[],
	clickHandler=null, icon=null,
	target=null, text
}){
	let element;
	const items = clist.join(" ");

	if (href){
		element = <Link to={href} id={id}
		className={items ? items : ""}
		onClick={ clickHandler }
		target={target ? target : "" }>
			{text}
			{icon ?
			<span>
				<FontAwesomeIcon
				icon={icon}/>
			</span> : ""
			}
		</Link>;
	} else {
		element = <button
		type="button" id={id}
		className={items ? items : ""}
		onClick={ clickHandler }>
			{text}
			{icon ?
				<span>
					<FontAwesomeIcon
				icon={icon}/>
				</span> : ""
			}
		</button>
	}
	return (<>{element}</>);
}
