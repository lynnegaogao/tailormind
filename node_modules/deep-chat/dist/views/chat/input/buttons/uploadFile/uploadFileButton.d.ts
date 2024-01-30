import { FileAttachmentsType } from '../../fileAttachments/fileAttachmentTypes/fileAttachmentsType';
import { GenericInputButtonStyles } from '../../../../../types/genericInputButton';
import { DefinedButtonStateStyles } from '../../../../../types/buttonInternal';
import { FileServiceIO } from '../../../../../services/serviceIO';
import { InputButton } from '../inputButton';
type Styles = DefinedButtonStateStyles<GenericInputButtonStyles>;
export declare class UploadFileButton extends InputButton<Styles> {
    private readonly _inputElement;
    private readonly _fileAttachmentsType;
    private _openModalOnce?;
    constructor(containerElement: HTMLElement, fileAttachmentsType: FileAttachmentsType, fileService: FileServiceIO, iconId: string, iconSVGString: string, dropupText?: string);
    private createInnerElements;
    private triggerImportPrompt;
    private import;
    private static createInputElement;
    private createInnerElement;
    private static createButtonElement;
    private static createSVGIconElement;
    private addClickEvent;
    private click;
}
export {};
//# sourceMappingURL=uploadFileButton.d.ts.map