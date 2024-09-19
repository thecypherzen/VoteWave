import { classNameFromList } from '../utils/createClassNames';
import styles from '../styles/heading.module.css';

export default function Heading({clist=null, main=false, runner=null, rclist=null, text}){
	const hClassName = classNameFromList(clist);
	const rClassName = classNameFromList(rclist);
	let divClassName = "";
	if (main) {
		divClassName += `${styles.heading} ${styles.main}`;
	} else {
		divClassName = styles.headingBox;
	}
	return (
		<div className={divClassName}>
			<h2 className={hClassName}>{text}
			</h2>
			{runner ? <p className={rClassName}>
				{runner}
			</p> : ""}
		</div>
	);
}