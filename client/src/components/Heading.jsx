import { classNameFromList } from '../utils/createClassNames';
import styles from '../styles/heading.module.css';

export default function Heading({clist=null, swoosh=null, main=false, text}){
	const hClassName = classNameFromList(clist);
	const sClassName = classNameFromList(swoosh);
	let divClassName = "";
	if (main) {
		divClassName += `${styles.heading} ${styles.main}`;
	}
	return (
		<div className={divClassName}>
			<h2 className={hClassName}>{text}</h2>
			{swoosh ?
			<span className={sClassName}>
			</span> : ""}
		</div>
	);
}