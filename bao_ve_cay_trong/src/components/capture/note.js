import React, { useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { TouchableOpacity } from 'react-native-gesture-handler';
import Icon from 'react-native-vector-icons/FontAwesome5';
import { SvgCss } from 'react-native-svg';
import CloseDuotone from 'assests/imgs/crops/svgs/close-duotone.svg';

const Note = ({ style, hide = false }) => {
	const [close, setClose] = useState(false);
	const handleClose = () => setClose(true);

	if (hide || close) return null;
	return (
		<View style={style}>
			<View style={styles.boudingBox}>
				<View style={styles.closeButton}>
					<TouchableOpacity onPress={handleClose}>
						<View style={styles.boudingButton}>
							<SvgCss
								width={20}
								height={20}
								color='white'
								xml={CloseDuotone}
							/>
						</View>
					</TouchableOpacity>
				</View>
				<Text style={styles.text}>
					Chụp nhiều ảnh ở các góc độ khác nhau để cải thiện độ chính
					xác
				</Text>
			</View>
		</View>
	);
};

const styles = StyleSheet.create({
	boudingBox: { position: 'relative', padding: 4 },
	boudingButton: {
		padding: 8,
	},
	closeButton: {
		// backgroundColor: 'red',
		position: 'absolute',
		right: -16,
		top: -18,
	},
	icon: {
		backgroundColor: 'black',
		borderRadius: 50,
		// padding: 2,
	},
	text: {
		width: '100%',
		height: '100%',
		color: 'white',
		textAlign: 'center',
	},
});

export default Note;
