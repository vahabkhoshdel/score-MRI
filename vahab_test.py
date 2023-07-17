import torch
import numpy as np
from pathlib import Path


from torch.utils.data import Dataset, DataLoader

class fastmri_knee(Dataset):
  """ Simple pytorch dataset for fastmri knee singlecoil dataset """
  def __init__(self, root, is_complex=False):
    self.root = root
    self.data_list = list(root.glob('*/*.npy'))
    print(self.data_list)

    self.is_complex = is_complex

  def __len__(self):
    return len(self.data_list)

  def __getitem__(self, idx):
    fname = self.data_list[idx]
    if not self.is_complex:
      data = np.load(fname).astype(np.float32)
    else:
      data = np.load(fname).astype(np.complex64)
    data = np.expand_dims(data, axis=0)
    return data



train_dataset = fastmri_knee(Path('/Users/khoshdev/Documents/Visual_Codes/score-MRI/media'))


print(type(train_dataset))
print("Size of the array:", train_dataset.size)
print("Dimensions of the array:", train_dataset.shape)



root = Path('/Users/khoshdev/Documents/Visual_Codes/score-MRI/media')
data_list = list(root.glob('*/*.npy'))
print(data_list)


# Display the size and dimensions
print("Size of the array:", data.size)
print("Dimensions of the array:", data.shape)

