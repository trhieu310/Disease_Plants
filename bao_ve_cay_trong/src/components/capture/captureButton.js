import React, { useState } from 'react';
import { StyleSheet, TouchableWithoutFeedback, View } from 'react-native';
import Icon from 'react-native-vector-icons/FontAwesome5';

const CaptureButton = ({
	size = 16,
	color = 'white',
	style = {},
	onPress,
	disabled = false,
	...props
}) => {
	const [isPressed, setPressed] = useState(false);

	const handlePressIn = () => {
		setPressed(true);
	};

	const handlePressOut = () => {
		setPressed(false);
	};

	return (
		<View style={[styles.container, style]}>
			<TouchableWithoutFeedback
				onPress={onPress}
				onPressIn={handlePressIn}
				onPressOut={handlePressOut}
				disabled={disabled}>
				<View>
					<View style={styles.underLayout}>
						<Icon
							style={{
								...styles.circleBase,
								opacity: isPressed ? 0.6 : 0.5,
							}}
							name='circle'
							size={size}
							color={color}
							solid
						/>
					</View>
					<View style={styles.aboveLayout}>
						<View style={styles.flexCenter}>
							<Icon
								style={{
									...styles.transistion,
									opacity: isPressed ? 0.7 : 1,
								}}
								name='circle'
								size={(size * 3) / 4}
								color={color}
								solid
							/>
						</View>
					</View>
				</View>
			</TouchableWithoutFeedback>
		</View>
	);
};

const styles = StyleSheet.create({
	container: {},
	circleBase: {
		opacity: 0.5,
	},
	underLayout: { position: 'relative' },

	aboveLayout: {
		position: 'absolute',
		// top: 0,
		// right: 0,
		width: '100%',
		height: '100%',
	},
	flexCenter: {
		width: '100%',
		height: '100%',
		position: 'relative',
		display: 'flex',
		justifyContent: 'center',
		alignItems: 'center',
		flex: 1,
	},
	transistion: {},
});

export default CaptureButton;
