from typing import Any, Dict, Optional, Tuple, Union, final, overload

import numpy

from pygame.event import Event

from . import mixer_music
from ._common import FileArg

# export mixer_music as mixer.music
music = mixer_music

def init(
    frequency: int = 44100,
    size: int = -16,
    channels: int = 2,
    buffer: int = 512,
    devicename: Optional[str] = None,
    allowedchanges: int = 5,
) -> None: ...
def pre_init(
    frequency: int = 44100,
    size: int = -16,
    channels: int = 2,
    buffer: int = 512,
    devicename: Optional[str] = None,
    allowedchanges: int = 5,
) -> None: ...
def quit() -> None: ...
def get_init() -> Tuple[int, int, int]: ...
def stop() -> None: ...
def pause() -> None: ...
def unpause() -> None: ...
def fadeout(time: int) -> None: ...
def set_num_channels(count: int) -> None: ...
def get_num_channels() -> int: ...
def set_reserved(count: int) -> int: ...
def find_channel(force: bool = False) -> Channel: ...
def get_busy() -> bool: ...
def get_sdl_mixer_version(linked: bool = True) -> Tuple[int, int, int]: ...

class Sound:
    @overload
    def __init__(self, file: FileArg) -> None: ...
    @overload
    def __init__(
        self, buffer: Any
    ) -> None: ...  # Buffer protocol is still not implemented in typing
    @overload
    def __init__(
        self, array: numpy.ndarray
    ) -> None: ...  # Buffer protocol is still not implemented in typing
    def play(
        self,
        loops: int = 0,
        maxtime: int = 0,
        fade_ms: int = 0,
    ) -> Channel: ...
    # possibly going to be deprecated/removed soon, in which case these
    # typestubs must be removed too
    __array_interface__: Dict[str, Any]
    __array_struct__: Any
    def stop(self) -> None: ...
    def fadeout(self, time: int) -> None: ...
    def set_volume(self, value: float) -> None: ...
    def get_volume(self) -> float: ...
    def get_num_channels(self) -> int: ...
    def get_length(self) -> float: ...
    def get_raw(self) -> bytes: ...

@final
class Channel:
    def __init__(self, id: int) -> None: ...
    def play(
        self,
        sound: Sound,
        loops: int = 0,
        maxtime: int = 0,
        fade_ms: int = 0,
    ) -> None: ...
    def stop(self) -> None: ...
    def pause(self) -> None: ...
    def unpause(self) -> None: ...
    def fadeout(self, time: int) -> None: ...
    def queue(self, sound: Sound) -> None: ...
    def set_source_location(self, angle:float, distance:float) -> None: ...
    @overload
    def set_volume(self, value: float) -> None: ...
    @overload
    def set_volume(self, left: float, right: float) -> None: ...
    def get_volume(self) -> float: ...
    def get_busy(self) -> bool: ...
    def get_sound(self) -> Sound: ...
    def get_queue(self) -> Sound: ...
    def set_endevent(self, type: Union[int, Event] = 0) -> None: ...
    def get_endevent(self) -> int: ...

SoundType = Sound
ChannelType = Channel
