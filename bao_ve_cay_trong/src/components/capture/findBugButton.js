import React, { useState } from 'react';
import {
	StyleSheet,
	TouchableOpacity,
	TouchableWithoutFeedback,
	View,
} from 'react-native';
import { SvgCss } from 'react-native-svg';
import FindBugSvg from 'assests/imgs/crops/svgs/find-bug2.svg';

const FindBugButton = ({
	size = 16,
	color = 'white',
	style = {},
	onPress,
	disabled = false,
	hide = false,
	...props
}) => {
	// const [isPressed, setPressed] = useState(false);

	// const handlePressIn = () => {
	// 	setPressed(true);
	// };

	// const handlePressOut = () => {
	// 	setPressed(false);
	// };

	if (hide) return null;

	return (
		<View style={[styles.container, style]}>
			<TouchableOpacity
				activeOpacity={0.7}
				onPress={onPress}
				// onPressIn={handlePressIn}
				// onPressOut={handlePressOut}
				disabled={disabled}>
				<View>
					<SvgCss
						width={size}
						height={size}
						color={color}
						xml={FindBugSvg}
					/>
				</View>
			</TouchableOpacity>
		</View>
	);
};

const styles = StyleSheet.create({
	container: {},
});

export default FindBugButton;
