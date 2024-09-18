import Button from './Button';
import styles from "../styles/section.module.css";

export default function SectionText({heading, body, button}){
	return (<>
	<div clasName={styles.sectionText}>
		<h2 clasName={styles.sectionHeading}>{heading}</h2>
		<p className={styles.sectionBody}>{body}</p>
		<Button href={button.href} id={button.id}
				clickHandler={button.clickHandler}
				text={button.text} clist={button.clist}/>
	</div>
	</>);
}