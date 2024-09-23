import styles from '../styles/emailverificationpage.module.css';
export default function EmailVerificationPage(){
	return (
		<div className={styles.content}>
			<h2>One more step</h2>
			<p>We've sent a verification link to your email. Please click it to complete your login.</p>
		</div>
	)
}