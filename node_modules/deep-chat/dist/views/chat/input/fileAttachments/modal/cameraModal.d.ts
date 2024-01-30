import { FileAttachmentsType } from '../fileAttachmentTypes/fileAttachmentsType';
import { CameraFiles } from '../../../../../types/camera';
import { CustomStyle } from '../../../../../types/styles';
import { Modal } from './modal';
export declare class CameraModal extends Modal {
    private _dataURL?;
    private _stopped;
    private readonly _captureButton;
    private readonly _submitButton;
    private readonly _canvas;
    private readonly _captureIcon;
    private readonly _refreshIcon;
    private _mediaStream?;
    private readonly _format;
    private readonly _newFilePrefix?;
    private readonly _dimensions?;
    constructor(viewContainerElement: HTMLElement, fileAttachmentsType: FileAttachmentsType, containerStyle?: CustomStyle, cameraFiles?: CameraFiles);
    private addButtonsAndTheirEvents;
    private addButtonEvents;
    private stop;
    start(): void;
    private capture;
    private getFile;
    private updateCanvas;
    private openCameraModal;
    static createCameraModalFunc(viewContainerElement: HTMLElement, fileAttachmentsType: FileAttachmentsType, modalContainerStyle?: CustomStyle, cameraFiles?: CameraFiles): () => void;
}
//# sourceMappingURL=cameraModal.d.ts.map