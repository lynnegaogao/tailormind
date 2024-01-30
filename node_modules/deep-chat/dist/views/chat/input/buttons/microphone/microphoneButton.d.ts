import { DefinedButtonStateStyles } from '../../../../../types/buttonInternal';
import { MicrophoneStyles } from '../../../../../types/microphone';
import { ButtonStyles } from '../../../../../types/button';
import { InputButton } from '../inputButton';
type AllMicrophoneStyles = MicrophoneStyles & {
    commandMode?: ButtonStyles;
};
type Styles = DefinedButtonStateStyles<AllMicrophoneStyles>;
export declare class MicrophoneButton extends InputButton<Styles> {
    private readonly _innerElements;
    isActive: boolean;
    constructor(styles?: AllMicrophoneStyles);
    private createInnerElements;
    private createInnerElement;
    private static createMicrophoneElement;
    private static createSVGIconElement;
    changeToActive(): void;
    changeToDefault(): void;
    changeToCommandMode(): void;
    changeToUnsupported(): void;
    private toggleIconFilter;
}
export {};
//# sourceMappingURL=microphoneButton.d.ts.map