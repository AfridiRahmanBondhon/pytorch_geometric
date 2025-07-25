from collections import defaultdict

import torch
import torch_geometric.typing

from ._compile import compile, is_compiling
from ._onnx import is_in_onnx_export
from .index import Index
from .edge_index import EdgeIndex
from .hash_tensor import HashTensor
from .seed import seed_everything
from .home import get_home_dir, set_home_dir
from .device import is_mps_available, is_xpu_available, device
from .isinstance import is_torch_instance
from .debug import is_debug_enabled, debug, set_debug

import torch_geometric.utils
import torch_geometric.data
import torch_geometric.sampler
import torch_geometric.loader
import torch_geometric.transforms
import torch_geometric.datasets
import torch_geometric.nn
import torch_geometric.explain
import torch_geometric.profile

from .experimental import (is_experimental_mode_enabled, experimental_mode,
                           set_experimental_mode)
from .lazy_loader import LazyLoader

contrib = LazyLoader('contrib', globals(), 'torch_geometric.contrib')
graphgym = LazyLoader('graphgym', globals(), 'torch_geometric.graphgym')

__version__ = '2.7.0'

__all__ = [
    'Index',
    'EdgeIndex',
    'HashTensor',
    'seed_everything',
    'get_home_dir',
    'set_home_dir',
    'compile',
    'is_compiling',
    'is_in_onnx_export',
    'is_mps_available',
    'is_xpu_available',
    'device',
    'is_torch_instance',
    'is_debug_enabled',
    'debug',
    'set_debug',
    'is_experimental_mode_enabled',
    'experimental_mode',
    'set_experimental_mode',
    'torch_geometric',
    '__version__',
]

if not torch_geometric.typing.WITH_PT113:
    import warnings as std_warnings

    std_warnings.warn(
        "PyG 2.7 removed support for PyTorch < 1.13. Consider "
        "Consider upgrading to PyTorch >= 1.13 or downgrading "
        "to PyG <= 2.6. ", stacklevel=2)

# Serialization ###############################################################

if torch_geometric.typing.WITH_PT24:
    torch.serialization.add_safe_globals([
        dict,
        list,
        defaultdict,
        Index,
        torch_geometric.index.CatMetadata,
        EdgeIndex,
        torch_geometric.edge_index.SortOrder,
        torch_geometric.edge_index.CatMetadata,
        HashTensor,
    ])
