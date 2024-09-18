/* Defines the landing page */
import NavBar from '../components/NavBar';
import Section, {
	SectionImage,
	SectionText
} from '../components/Section';
import { faArrowRight } from '@fortawesome/free-solid-svg-icons';
import styles from '../styles/section.module.css';

export default function Landing(){
	return (
		<>
		<NavBar />
		<Section id="hero-section" clsname={styles.landingSection}>
			<SectionText
				heading="Goodbye to boring voting experiences."
				body="Now you can vote, play and chat all at once. Join a poll or election to begin."
				button={{
					href: "/activities",
					text: "Join activity",
					clist: ["btn", "btn-secondary"],
					icon: faArrowRight
				}}/>
			<SectionImage />
		</Section>
		</>
	);
}