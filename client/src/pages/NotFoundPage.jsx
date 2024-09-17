import Button from '../components/Button';
import styles from "../styles/notfoundpage.module.css";

export default function NotFound(){
	return(
	<>
	<div className={styles.content}>
		<h1>We couldn't find that.</h1>
		<p>For now let's take you back home.</p>
		<div className={styles.button}>
			<Button clist={["btn", "btn-secondary"]}
				text={"Return home"} href="/" />
		</div>
	</div>
	</>
	);
}