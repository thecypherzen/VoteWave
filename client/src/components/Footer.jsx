import Wrapper from './Wrapper';
import styles from '../styles/footer.module.css'

export default function Footer(){
	return (
		<footer className={styles.footer}>
			<Wrapper>
				<div className={styles.content}>
					<p>VoteWave &copy; 2024</p>
				</div>
			</Wrapper>
		</footer>
	);
}