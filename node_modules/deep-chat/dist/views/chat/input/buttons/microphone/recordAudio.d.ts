import { AudioFileAttachmentType } from '../../fileAttachments/fileAttachmentTypes/audioFileAttachmentType';
import { MicrophoneFilesServiceConfig } from '../../../../../types/fileServiceConfigs';
import { MicrophoneButton } from './microphoneButton';
export declare class RecordAudio extends MicrophoneButton {
    private _mediaRecorder?;
    private _mediaStream?;
    private _waitingForBrowserApproval;
    private readonly _audioType;
    private readonly _extension;
    private readonly _maxDurationSeconds?;
    private readonly _newFilePrefix?;
    constructor(audioType: AudioFileAttachmentType, recordAudioConfig: MicrophoneFilesServiceConfig);
    private buttonClick;
    private stop;
    private record;
    private createFile;
}
//# sourceMappingURL=recordAudio.d.ts.map