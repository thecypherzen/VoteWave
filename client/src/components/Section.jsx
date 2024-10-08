import Button from './Button';
import Heading from './Heading';
import Wrapper from './Wrapper';
import styles from "../styles/section.module.css";




export default function Section({ id, clsname, children }){
	return (
	<section id={styles[id]} className={clsname}>
		<Wrapper clist={[styles.sectionWrapper]}>
			{children}
		</Wrapper>
	</section>
	);
}


export  function SectionImage({id=null}){
	return(
	<div id={styles[id]} className={styles.sectionImage}>
	</div>
	);
}


export function SectionText({heading, body, button}){
	return (
	<>
		<div className={styles.sectionText}>
			<Heading
				clist={[styles.sectionHeading]}
				text={heading}/>
			<p className={styles.sectionBody}>{body}</p>
			<div className={styles.sectionBtn}>
				<Button href={button.href} id={button.id}
						clickHandler={button.clickHandler}
						text={button.text} clist={button.clist}
						icon={button.icon}
						target={button.target}/>
			</div>
		</div>
	</>
	);
}