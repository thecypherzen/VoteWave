/* Defines the landing page */
import Heading from '../components/Heading';
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
		<Heading clist={[styles.sectionHeading, styles.center]}
				swoosh={[styles.swoosh, styles.accent]}
				main={true}
				text="Features" />
		<Section id="features-section" clsname={styles.landingSection}>
			<SectionText
				heading="Create elections and opinion polls."
				body="Elections require candidates and deny multiple voting while polls don't require candidates and allow multiple votes...You'd get a hang of it when you create one."
				button={{
					href: "/login",
					text: "Get started",
					clist: ["btn", "btn-secondary"],
					icon: faArrowRight
				}}/>
			<SectionImage />
		</Section>
		</>
	);
}